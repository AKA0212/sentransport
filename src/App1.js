import './App.css';
import Header from './Header';
import Footer from './Footer';
import Statistique from './Statistique';
import LigneBus from './LigneBus';


function App() {
  return (
    <div className="App">
      <Header />
      <main className="contenu">
        <LigneBus
          numero="15"
          depart="Parcelles Assainies"
          arrivee="Plateau"
          arrets={14}
        />
        <LigneBus
          numero="7"
          depart="Guediawaye"
          arrivee="Place Obélisque"
          arrets={18}
        />
      </main>
    </div>
  );
}

const App = () => 
<div className = " App">
  <Header />
  <main className = " contenu " >
    <p> Bienvenue ! Cette application vous aide a trouver votre ligne de bus a Dakar . </p>
    <Statistique />
    <Statistique />
    <Statistique />
  </ main >
  <Footer />
</div >;


export default App ;