import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
`;

export const Tittle = styled.h1`
  font-size: 30px;

  font-variant: small-caps;
  flex: 1;
  margin-top: 40px;

  @media screen and (min-width: 500px) {
    font-size: 40px;
  }

  @media screen and (min-width: 720px) {
    font-size: 60px;
  }
`;

export const MainImageContainer = styled.div`
  height: 60vh;
  width: 80vw;

  @media screen and (min-width: 720px) {
    height: 70vh;
    width: 60vw;
  }

  @media screen and (min-width: 1000px) {
    height: 70vh;
    width: 50vw;
  }
`;
