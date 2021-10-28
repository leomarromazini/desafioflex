import "./App.css";
import Header from "./components/Header";
import Routes from "./routes";

import { GlobalStyles } from "./styles/global.js";
function App() {
  return (
    <>
      <GlobalStyles />
      <Header />
      <div className="App" style={{ display: "flex" }}>
        <Routes />
      </div>
    </>
  );
}

export default App;
