DROP TABLE IF EXISTS appointments;

CREATE TABLE appointments (
  id serial primary key,
  name varchar(200) not null,
  start_datetime timestamp not null,
  end_datetime timestamp not null,
  description text not null,
  private boolean not null
);

INSERT INTO appointments (
  name, start_datetime, end_datetime, description, private
)
VALUES (
  'My appointment',
  datetime(date(CURRENT_TIMESTAMP), '+14 hours'),
  datetime(date(CURRENT_TIMESTAMP), '+15 hours'),
  'An appointment for me',
  false
);


