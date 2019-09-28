import React from "react";
import ReactDOM from "react-dom";
import MasterDataProvider from "./MasterDataProvider";
import SymptomSelect from "./SymptomSelect";
const App = () => (
  <div>
    <strong>Symptom Checker</strong>
    <hr />
    <h3>Please select your symptom</h3>
    <hr />
    <MasterDataProvider
      render={(symptom_data, diagnosis_data) => (
        <SymptomSelect data={{ ...{ symptom_data }, ...{ diagnosis_data } }} />
      )}
    />
  </div>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
