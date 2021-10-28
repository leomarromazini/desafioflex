import { CertificateProvider } from "./Certificates";

const Providers = ({ children }) => {
  return <CertificateProvider>{children}</CertificateProvider>;
};

export default Providers;
