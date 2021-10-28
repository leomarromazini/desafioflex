import axios from "axios";

const api = axios.create({
  baseURL: "https://desafio-flex-back-end.herokuapp.com",
});

export default api;
