import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';

const ReportShow = () => {
    const { reportId } = useParams();
    const report = useSelector((store) => store.reports[reportId]);

    return (
        <section>
            ID: {report.id}
            <br />
            Understanding: {report.understanding}
            <br />
            Improvement: {report.improvement}
            <br />
            <Link to="/">Back to Report Index</Link>
        </section>
    );
};

export default ReportShow;
