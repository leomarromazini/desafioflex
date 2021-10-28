import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import HomeIcon from "@mui/icons-material/Home";

import { useHistory } from "react-router";

const StyledToolbar = styled(Toolbar)(({ theme }) => ({
  alignItems: "center",
  paddingTop: theme.spacing(1),
  paddingBottom: theme.spacing(1),
  backgroundColor: "var(--header)",
  "@media all": {
    minHeight: 60,
  },
}));

const Header = () => {
  const history = useHistory();

  const sendTo = (path) => {
    history.push(path);
  };
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <StyledToolbar variant="dense">
          <IconButton
            edge="start"
            aria-label="menu"
            sx={{ mr: 2, color: "var(--white)" }}
            onClick={() => sendTo("/")}
          >
            <HomeIcon fontSize="large" />
          </IconButton>
          <IconButton color="inherit">
            <Typography
              variant="h5"
              sx={{
                fontSize: "30px",
                cursor: "pointer",
                marginTop: 0.5,
                color: "var(--white)",
              }}
              color="inherit"
              component="div"
              onClick={() => sendTo("/dashboard")}
            >
              Certificados
            </Typography>
          </IconButton>
        </StyledToolbar>
      </AppBar>
    </Box>
  );
};

export default Header;
