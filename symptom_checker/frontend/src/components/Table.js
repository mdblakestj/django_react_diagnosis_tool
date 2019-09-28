import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
const Table = ({ data }) =>
  !data.symptom_count.length ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      <h2 className="subtitle">
        Showing <h1>{data.symptom_count.length} most frequent diagnoses</h1>
      </h2>
      <table className="table is-striped">
        <thead>
          <tr>
            {data.symptom_count.map(el => (
              <th key={key(el)}>
                {data.diagnosis_data[el.diagnosis_id - 1].name}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.symptom_count.map(el => (
            <td key={key(el)}>{el.id__count}</td>
          ))}
        </tbody>
      </table>
    </div>
  );

export default Table;
