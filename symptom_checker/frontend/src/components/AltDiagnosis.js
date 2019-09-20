import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import axios from "axios";
import Table from "./Table";
import key from "weak-key";

export default class AltDiagnosis extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  sendToDb(diagnosis_id) {
    axios
      .post(
        "/api/symptomdiagnosis/",
        { symptom: this.props.data.symptom_id, diagnosis: diagnosis_id },
        { headers: { "Content-Type": "application/json" } }
      )
      .then();
  }
  _refreshPage() {
    window.location.reload();
  }
  render() {
    return (
      <div>
        <h1>Please Choose An Alternate Illness </h1>

        <DataProvider
          endpoint="api/symptomdiagnosis/"
          render={data => (
            <div>
              <div class="select">
                <select
                  onChange={e => {
                    var diagnosis = e.target.value;

                    let obj = this.props.data.diagnosis_data.find(
                      obj => obj.name == diagnosis
                    );
                    let selected = true;
                    this.setState(() => ({ selected }));
                    let diagnosis_id = obj.id;
                    this.sendToDb(diagnosis_id);
                  }}
                >
                  {" "}
                  <option />
                  {data
                    .filter(
                      diag =>
                        diag.symptom == this.props.data.symptom_id &&
                        diag.diagnosis != this.props.data.diag_id
                    )
                    .map(
                      symptom =>
                        this.props.data.diagnosis_data[symptom.diagnosis - 1]
                          .name
                    )
                    .map(symptom => (
                      <option key={symptom}>{symptom}</option>
                    ))}
                </select>
              </div>
            </div>
          )}
        />
        {this.state.selected && (
          <div>
            <DataProvider
              endpoint={`api/symptom/${this.props.data.symptom_id}/likely/`}
              render={data => (
                <Table
                  data={{
                    ...{ symptom_count: data },
                    ...{ diagnosis_data: this.props.data.diagnosis_data }
                  }}
                />
              )}
            />
            <button onClick={this._refreshPage}> Start Over </button>{" "}
          </div>
        )}
      </div>
    );
  }
}
