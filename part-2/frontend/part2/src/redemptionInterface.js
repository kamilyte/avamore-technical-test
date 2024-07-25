import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./styles.css"

// web interface for the redemption model
function RedemptionInterface() {
  // stores the state of the answer
  const [answer, setAnswer] = useState("");
  
  // the state of the import form
  const [data, setData] = useState({
    facilitya: 0,
    monthlyRate: 0,
    beginningDefaultPeriod: "",
    endDefaultPeriod: ""
  });

  // handles the changes of the input form
  const handleChange = (e) => {
    const value = e.target.value;
    setData({...data, [e.target.name]: value});
  };

  // submits the flexible inputs to the post api endpoint and retrieves the total interest due
  const handleSubmit = (e) => {
    e.preventDefault();

    // retrieve the data
    const userData = {
      facilitya: data.facilitya,
      monthlyRate: data.monthlyRate,
      beginningDefaultPeriod: data.beginningDefaultPeriod,
      endDefaultPeriod: data.endDefaultPeriod,
    };

    // make post request and change state of the answer
    axios.post("http://localhost:8000", userData).then((response) => {
      console.log(response.status, response.data.token)
      setAnswer(response.data.answer);  
    });
  };

  // identifies whether the date is in the right format
  useEffect(() => {
    const inputs = document.querySelectorAll("[date-input]");

    const handleInput = (event) => {
      const value = event.target.value.toUpperCase();
      const datePattern = /^(0?[1-9]|[12][0-9]|3[01])-(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)-(\d{2})$/;

      if (!datePattern.test(value)) {
        event.target.setCustomValidity('Invalid date format. Use DD-MMM-YY');
      } else {
        event.target.setCustomValidity('');
      };
    };

    inputs.forEach((input) => {
      input.addEventListener("input", handleInput);
    });

    return () => {
      inputs.forEach((input) => {
        input.removeEventListener("input", handleInput);
      });
    };
  }, []);

  return (
    <div>
      <h1>Redemption Model</h1>
      <form onSubmit={handleSubmit}>
        <div className="input-container">
          <label htmlFor="facilitya">
            Facility A (Land Advance)
            <input type="number" name="facilitya" value={data.facilitya} onChange={handleChange} required />
          </label>
        </div>
        <div className="input-container">
          <label htmlFor="monthlyRate">
            Contractual Monthly Rate
            <input type="number" name="monthlyRate" value={data.monthlyRate} onChange={handleChange} required />
          </label>
        </div>
        <div className="input-container">
          <label htmlFor="beginningDefaultPeriod">
            Beginning of Default Period
            <input type="text" name="beginningDefaultPeriod" value={data.beginningDefaultPeriod} onChange={handleChange} date-input="true" required />
          </label>
        </div>
        <div className="input-container">
          <label htmlFor="endDefaultPeriod">
            End of Default Period
            <input type="text" name="endDefaultPeriod" value={data.endDefaultPeriod} onChange={handleChange} required date-input="true" />
          </label>
        </div>
        <button className='button-style' type="submit">SUBMIT</button>
      </form>
      <div className='answer-container'>
        <h2>Total interest due:</h2>
        <h2 className='answer-text'>{answer}</h2>
      </div>
    </div>
  );
}

export default RedemptionInterface;

