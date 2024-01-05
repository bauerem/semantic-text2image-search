import { useState } from 'react'
import logo from '/wheelwish.jpeg'
import './App.css'
import { Results } from '../components/Results'
import Header from '../components/Header';

const API_URL = "http://127.0.0.1:8000";


function App() {

  const [list, setList] = useState([]);
  const [textInput, setTextInput] = useState("");



  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      search(textInput)
        .then(() => {
          setTextInput("");
        })
    }
  }

  const search = (query) => {
    try {
      fetch(API_URL + '?query=' + query)
        .then((response) => response.json())
        .then((response) => {
          setList(response.result.documents[0])
        })
    } catch (error) {
      console.log('ERROR!', error);
    }
  }

  const onSubmit = () => {
    search(textInput)
      .then(() => {
        setTextInput("");
      })
  }

  const onChange = (e) => {
    setTextInput(e.target.value)
  }


  return (
    <div>
      <Header />
      <div style={{
        display: "flex",
        justifyContent: "center"
      }}>
        <a target="_blank">
          <img src={logo} className="logo" alt="Vite logo" />
        </a>
        <h1>WheelWish</h1>
      </div>

      <div style={{
        display: "flex",
        justifyContent: "center",
        width: "1280px"
      }}>
        <div>
          <p>
            Search for and retrieve objects visible from satellite imagery.
          </p>
          <p className="read-the-docs">
            This tool helps you to find examples. It is not an exhaustive search.
          </p>
          <div>
            <input
              style={{ marginTop: 10, marginBottom: 20, height: 30, width: "30vw" }}
              type="text"
              value={textInput}
              onChange={onChange}
            />
            <button style={{ width: "10vw", margin: 5 }} onClick={onSubmit} onKeyDown={handleKeyDown}>
              Search
            </button>
          </div>
          <div style={{ borderStyle: 'solid', width: "50vw", height: "50vh", overflowY: "scroll" }}>
            <Results list={list} />
          </div>
        </div>
      </div>
    </div>
  )
}

export default App