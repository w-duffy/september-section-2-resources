import { Link } from 'react-router-dom';
import ReportIndexItem from './ReportIndexItem';
import { useSelector, useDispatch } from 'react-redux';
import { resetReports } from '../store/reportsReducer';
import { getReports } from '../store/reportsReducer';

const ReportsIndex = () => {
    const dispatch = useDispatch();

    //! Best
    const reports = useSelector(getReports);

    //! Better
    // const reportData = useSelector((store) => store.reports);
    // const reports = Object.values(reportData);
    //! Bad
    // const reports = useSelector((store) => Object.values(store.reports));
    const resetData = (e) => {
        e.preventDefault();

        dispatch(resetReports());
    };

    return (
        <section>
            <ul>
                {reports.map((report) => (
                    <ReportIndexItem report={report} key={report.id} />
                ))}
            </ul>
            <Link to="/reports/new">New Report</Link>
            <button onClick={resetData}>Reset Data</button>
        </section>
    );
};

export default ReportsIndex;
