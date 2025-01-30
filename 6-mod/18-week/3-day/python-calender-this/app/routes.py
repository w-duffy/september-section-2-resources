from datetime import datetime, timedelta
from flask import Blueprint, redirect, render_template, url_for
from app.forms import AppointmentForm
import os
import sqlite3
import contextlib

bp = Blueprint("main", __name__, url_prefix="")
DB_FILE = os.environ.get("DB_FILE")

@bp.route("/")
def main():
    d = datetime.now()
    return redirect(url_for(".daily", year=d.year, month=d.month, day=d.day))


@bp.route("/<int:year>/<int:month>/<int:day>", methods=["GET", "POST"])
def daily(year, month, day):
    form = AppointmentForm()
    if form.validate_on_submit():
        with sqlite3.connect(DB_FILE) as conn:
            with contextlib.closing(conn.cursor()) as insert:
                sql = """
                    INSERT INTO appointments (
                        name,
                        start_datetime,
                        end_datetime,
                        description,
                        private
                    )
                    VALUES
                    (
                        :name,
                        :start_datetime,
                        :end_datetime,
                        :description,
                        :private
                    )
                """
                params = {
                    'name': form.name.data,
                    'start_datetime': round_time(datetime.combine(
                                        form.start_date.data,
                                        form.start_time.data,
                                        )),
                    'end_datetime': round_time(datetime.combine(
                                        form.end_date.data,
                                        form.end_time.data,
                                    )),
                    'description': form.description.data,
                    'private': form.private.data
                }
                insert.execute(sql, params)
                conn.commit()
                return redirect("/")
    with sqlite3.connect(DB_FILE) as conn:
        with contextlib.closing(conn.cursor()) as select:
            day = datetime(year, month, day)
            next_day = day + timedelta(days=1)
            sql = """
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                WHERE start_datetime BETWEEN :day AND :next_day
                ORDER BY start_datetime
            """
            select.execute(sql, {'day': day, 'next_day': next_day})
            raw_rows = select.fetchall()
            rows = []
            for raw_row in raw_rows:
                row = list(raw_row)
                row[2] = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                row[3] = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                rows.append(row)
            timeslots = [{'time': slot(day, slot_index, 8), 'open': True}
                            for slot_index in range(12 * 4)]
            overriden = 0
            for timeslot in timeslots:
                for id, name, start, end in rows:
                    if start == timeslot['time']:
                        timeslot['appointment'] = {
                            'units': int((end - start).seconds / 60 // 15),
                            'name': name,
                        }
                        overriden = timeslot['appointment']['units']
                if overriden > 0:
                    overriden -= 1
                    timeslot['open'] = False
            from pprint import pprint
            pprint(rows)
            return render_template("main.html",
                                    day=day,
                                    timeslots=timeslots,
                                    form=form)


def round_time(time):
    return time - timedelta(minutes=time.minute % 15,
                            seconds=time.second)


def slot(day, index, hours=0):
    day = datetime(day.year, day.month, day.day)
    day = day + timedelta(hours=hours)
    return day + timedelta(minutes=15 * index)
