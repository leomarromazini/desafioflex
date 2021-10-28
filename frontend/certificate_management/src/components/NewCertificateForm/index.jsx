import Box from "@mui/material/Box";
import Input from "@mui/material/Input";
import Button from "@mui/material/Button";
import { useCertificate } from "../../providers/Certificates";
import { useForm } from "react-hook-form";

const ariaLabel = { "aria-label": "description" };

const NewCertificateForm = () => {
  const { createCertificate } = useCertificate();

  const { register, handleSubmit } = useForm();

  const formOutputData = (data) => {
    console.log(data);
    createCertificate(data);
  };
  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <Box
        component="form"
        sx={{
          "& > :not(style)": { m: 1 },
        }}
        noValidate
        autoComplete="off"
        onSubmit={handleSubmit(formOutputData)}
      >
        <Input
          placeholder="Nome"
          inputProps={ariaLabel}
          {...register("name")}
        />
        <Input
          placeholder="Usuário"
          inputProps={ariaLabel}
          {...register("username")}
        />
        <Input
          placeholder="Descrição"
          inputProps={ariaLabel}
          {...register("description")}
        />
        <Input
          placeholder="Grupos"
          inputProps={ariaLabel}
          {...register("groups")}
        />

        <Input
          placeholder="Data de expiração"
          inputProps={ariaLabel}
          {...register("expiration")}
        />
        <Button type="submit" variant="contained">
          Enviar{" "}
        </Button>
      </Box>
      <Box></Box>
    </div>
  );
};

export default NewCertificateForm;
