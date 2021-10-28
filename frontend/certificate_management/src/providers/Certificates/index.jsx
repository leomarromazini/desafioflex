import { createContext, useContext, useState } from "react";

import api from "../../services";

export const CertificateContext = createContext([]);

export const CertificateProvider = ({ children }) => {
  const [certificates, setCertificates] = useState([]);

  const load_all_certificates = () => {
    api
      .get("/certificate", { mode: "cors" })
      .then((response) => setCertificates(response.data));
  };

  const createCertificate = (data) => {
    data.expiration = parseInt(data.expiration);
    data.groups = [data.groups];
    console.log(data);
    api.post("/certificate", data).then((response) => {
      console.log(response);
      const certificate = response.data;

      setCertificates([...certificates, certificate]);
    });
  };

  return (
    <CertificateContext.Provider
      value={{ load_all_certificates, certificates, createCertificate }}
    >
      {children}
    </CertificateContext.Provider>
  );
};

export const useCertificate = () => useContext(CertificateContext);
