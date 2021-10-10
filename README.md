# Object-Tracking-Algorithms

Este repositorio academico tiene el objetivo de demostrar el funcionamiento de algoritmos de Seguimiento que pertenecen a las siguientes familias:
 <ul> <li>Optical Flow</li></ul>  
 <ul> <li>Kalman Filter</li></ul> 
 <ul> <li>Particle Filter</li></ul> 

## Autores

- [@alandgabriel](https://www.github.com/alandgabriel)

 
## Contenido del curso
| No.        | Algoritmo           | Familia | Código  |  Referencias|
| :-------------: |:-------------| :-------------|:-----:| :-----|
| 1.              |   Lucas Kanade       | Optical Flow |   <ul> <li>[Código Fuente](/opticalFlow/src/LukasKanade.py)</li></ul>    | <ul><li> [Artículo](https://cecas.clemson.edu/~stb/klt/lucas_bruce_d_1981_1.pdf) </li></ul>
| 2.              |  Farneback     | Optical Flow |   <ul> <li>[Código Fuente](/opticalFlow/src/farneback.py)</li></ul>    |  <ul> <li> [Artículo](http://www.diva-portal.org/smash/get/diva2:273847/FULLTEXT01.pdf)</li> </ul>
| 3.              |  Kalman Filter   | Stochastic Filter |   <ul> <li>[Código Fuente](/kalman-filter/src/main.py)</li> </ul>    |  <ul><li>[Artículo](https://www.unitedthc.com/DSP/Kalman1960.pdf) <li> [Desarrollo Matemático](http://140.113.144.123/EnD106/Bayesian%20filtering-%20from%20Kalman%20filters%20to%20Particle%20filters%20and%20beyond.pdf) </li></ul>
| 4.              |Particle Filter  | Stochastic Filter |   <ul> <li>[Código Fuente](/particle-filter/src/particle_filter.py)</li> </ul>    |  <ul><li>[Artículo](http://robots.stanford.edu/papers/fox.aaai99.pdf)<li> [Implementación de referencia](http://140.113.144.123/EnD106/Bayesian%20filtering-%20from%20Kalman%20filters%20to%20Particle%20filters%20and%20beyond.pdf) <li> [Desarrollo Matemático](http://140.113.144.123/EnD106/Bayesian%20filtering-%20from%20Kalman%20filters%20to%20Particle%20filters%20and%20beyond.pdf) </li></ul> 



## Demo

Insert gif or link to demo

 ![alt text](figs/bg.png)
 
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

  
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```

  
## Running Tests

To run tests, run the following command

```bash
  npm run test
```

  
## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

