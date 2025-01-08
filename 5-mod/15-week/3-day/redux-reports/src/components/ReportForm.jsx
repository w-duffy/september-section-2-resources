import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import {
    receiveReport,
    // createReport,
    // updateReport,
} from '../store/reportsReducer';

const ReportForm = ({ report, formType }) => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [understanding, setUnderstanding] = useState(report.understanding);
    const [improvement, setImprovement] = useState(report.improvement);

    const handleSubmit = (e) => {
        e.preventDefault();
        report = { ...report, understanding, improvement };

        // //? createdAt example
        // if (formType === 'Update Report') {
        //     report.updatedAt = new Date();
        // }

        // if (formType === 'Update Report') dispatch(updateReport(report));
        // else dispatch(createReport(report));

        dispatch(receiveReport(report));

        navigate(`/reports/${report.id}`);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>{formType}</h2>
            <label>
                Understanding
                <input
                    type="text"
                    value={understanding}
                    onChange={(e) => setUnderstanding(e.target.value)}
                />
            </label>
            <label>
                Improvement
                <textarea
                    value={improvement}
                    onChange={(e) => setImprovement(e.target.value)}
                />
            </label>
            <input type="submit" value={formType} />
        </form>
    );
};

export default ReportForm;
