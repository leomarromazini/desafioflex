import { useEffect } from "react";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import { Container, BoxContainer } from "./styles.js";
import NewCertificateModal from "../NewCertificateModal";
import { useCertificate } from "../../providers/Certificates";
const CustomPaper = styled(Paper)(({ theme }) => ({
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: "center",
  color: theme.palette.text.secondary,
  minHeight: "70vh",
  minWidth: "50vw",
  display: "flex",
  flexDirection: "column",
  justifyContent: "space-between",
}));

// const { habits, habitsAchieved, loadHabits, loading } = useHabit();

function Dashboard() {
  const { load_all_certificates, certificates } = useCertificate();

  useEffect(() => {
    load_all_certificates();
    console.log(certificates);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <Container>
      <Box sx={{ flexGrow: 1 }}>
        <Grid
          container
          spacing={2}
          direction="row"
          justifyContent="center"
          alignItems="center"
        >
          <Grid item xs={9} md={9}>
            <CustomPaper elevation={8}>
              <BoxContainer>
                <Box sx={{ flexGrow: 1 }}>
                  <Grid
                    container
                    spacing={2}
                    direction="row"
                    justifyContent="center"
                    alignItems="center"
                  >
                    <Grid item xs={9} md={9}>
                      <h2>Meus certificados</h2>
                      {certificates.map((certificate, index) => (
                        <Paper
                          elevation={3}
                          key={index}
                          sx={{ margin: "20px 0" }}
                        >
                          <p>
                            Nome
                            <p style={{ fontWeight: "bold" }}>
                              {certificate.name}
                            </p>
                          </p>
                          <p>
                            descrição
                            <p style={{ fontWeight: "bold" }}>
                              {certificate.description}
                            </p>
                          </p>
                          <p>
                            Usuário
                            <p style={{ fontWeight: "bold" }}>
                              {certificate.username}
                            </p>
                          </p>
                          <p>
                            Criado em
                            <p style={{ fontWeight: "bold" }}>
                              {certificate.created_at}
                            </p>
                          </p>
                          <p>
                            Expira em
                            <p style={{ fontWeight: "bold" }}>
                              {certificate.expirated_at}
                            </p>
                          </p>
                        </Paper>
                      ))}
                    </Grid>
                  </Grid>
                </Box>
              </BoxContainer>
              <NewCertificateModal />
            </CustomPaper>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
}

export default Dashboard;
