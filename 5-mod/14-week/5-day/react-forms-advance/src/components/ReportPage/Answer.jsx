import { LIKERT_SCALE, NUM_LIKERT_OPTIONS } from '../SurveyPage/SurveyConstants';

function Answer({ question, value }) {
  switch (question.type) {
    case "mcq": { // Use {} so variables declared in case have limited scope
      let answer = question.options.find((option) => option.value === Number(value));
      return (
        <>
          <div className="answer-header">{question.stem}</div>
          <div className="answer-response">
            {value === "other" ? "Other" : answer.text}
          </div>
        </>
      );
    }
    case "likert":
      return (
        <>
          <div className="answer-header">
            {question.stimulus && question.stimulus.text} {question.stem}
          </div>
          <div className="answer-response">
            {value === "N/A" ? "N/A" : LIKERT_SCALE[question.scale][NUM_LIKERT_OPTIONS-value]}
          </div>
        </>
      );
    case "cr":
    default:
      return (
        <>
          <div className="answer-header">{question.stem}</div>
          <div className="answer-response">{value}</div>
        </>
      );
  }
}

export default Answer;
