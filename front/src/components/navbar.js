import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

// Replace Navbar brand for an icon or something related

function navegationBar() {
  return (
    <>
      <Navbar bg="primary" variant="dark">
        <Container>
          <Navbar.Brand href="#home">Navbar</Navbar.Brand> 
          <Nav className="me-auto">
            <Nav.Link href="#home">FALP</Nav.Link>
            <Nav.Link href="#informacion">Informacion</Nav.Link>
            <Nav.Link href="#contacto">Contacto</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default navegationBar;