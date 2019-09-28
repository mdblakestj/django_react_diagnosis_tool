import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import DataProvider from "./DataProvider";
import DiagnosisConfirm from "./DiagnosisConfirm";

export default class SymptomSelect extends React.Component {
  constructor(props) {
    super(props);
    this.state = { symptom: "", symptom_id: "" };
  }
  _refreshPage() {
    window.location.reload();
  }
  render() {
    return (
      <div>
        <div class="select">
          <select
            onChange={e => {
              var symptom = e.target.value;
              let obj = this.props.data.symptom_data.find(
                obj => obj.name == symptom
              );
              let symptom_id = obj.id;
              this.setState(() => ({ symptom_id, symptom }));
            }}
          >
            {" "}
            <option />
            {this.props.data.symptom_data.map(symptom => (
              <option key={key(symptom)}>{symptom.name}</option>
            ))}
          </select>
          {this.state.symptom_id && (
            <DataProvider
              endpoint={`api/symptom/${this.state.symptom_id}/likely/`}
              render={data => (
                <DiagnosisConfirm
                  data={{
                    ...{ symptom_count: data },
                    ...this.state,
                    ...{ diagnosis_data: this.props.data.diagnosis_data },
                    ...{ symptom_data: this.props.data.symptom_data }
                  }}
                />
              )}
            />
          )}
        </div>
      </div>
    );
  }
}
