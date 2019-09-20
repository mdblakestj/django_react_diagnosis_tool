import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import DataProvider from "./DataProvider";
import AltDiagnosis from "./AltDiagnosis";
import Table from "./Table";

export default class DiagnosisConfirm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { symptom_id: 3, answer: "" };
  }
  topDiagnosis = (diags, data) => {
    let sorted = diags.sort((a, b) => (a.id__count > b.id__count ? 1 : -1));

    let obj_array = data.filter(
      obj => obj.id == sorted[diags.length - 1].diagnosis_id
    );
    let diag_id = obj_array[0].id;
    this.setState(() => ({ diag_id }));
    if (obj_array.length > 1) {
      let diagnosis = obj_array[Math.floor(Math.random() * obj_array.length)];
      this.setState(() => ({ diagnosis }));
    }

    let obj = data.find(obj => obj.id == obj_array[0].diagnosis_id);

    let diagnosis = obj_array[0].name;
    this.setState(() => ({ diagnosis }));
  };
  _refreshPage() {
    window.location.reload();
  }

  componentWillMount() {
    let symptom_id = this.props.data.symptom_id;
    this.setState(() => ({ symptom_id }));
    this.topDiagnosis(
      this.props.data.symptom_count,
      this.props.data.diagnosis_data
    );
  }

  render() {
    return (
      <div>
        <h1 />
        <div>
          <h1>Do you have {this.state.diagnosis}?</h1>
          <div class="select">
            <select
              onChange={e => {
                var answer = e.target.value;
                this.setState(() => ({ answer }));
              }}
            >
              {" "}
              <option />
              <option value="Yes">Yes</option>
              <option value="No">No</option>
            </select>
            {this.state.answer == "Yes" && (
              <div>
                <h1>Thank You!</h1>
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
            {this.state.answer == "No" && (
              <AltDiagnosis
                data={{
                  ...this.state,
                  ...{ diagnosis_data: this.props.data.diagnosis_data },
                  ...{ symptom_data: this.props.data.symptom_data }
                }}
              />
            )}
          </div>
        </div>
      </div>
    );
  }
}
