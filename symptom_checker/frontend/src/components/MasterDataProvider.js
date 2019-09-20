import React, { Component } from "react";
import PropTypes from "prop-types";
class MasterDataProvider extends Component {
  static propTypes = {
    render: PropTypes.func.isRequired
  };
  state = {
    diagnosis_data: [],
    symptom_data: [],
    loaded: false,
    placeholder: "Loading..."
  };
  componentDidMount() {
    fetch("api/symptom/")
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong" });
        }
        return response.json();
      })
      .then(data => this.setState({ symptom_data: data, loaded: true }));
    fetch("api/diagnosis/")
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong" });
        }
        return response.json();
      })
      .then(data => this.setState({ diagnosis_data: data, loaded: true }));
  }
  render() {
    const { diagnosis_data, symptom_data, loaded, placeholder } = this.state;
    return loaded ? (
      this.props.render(symptom_data, diagnosis_data)
    ) : (
      <p>{placeholder}</p>
    );
  }
}
export default MasterDataProvider;
