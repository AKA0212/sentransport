import "./Recherche.css";

function Recherche({ valeur, onChange }) {

    function handleEffacer() {
        onChange("");
    }

    return (
        <div className="recherche">

            <input
                type="text"
                className="recherche-input"
                placeholder="Rechercher une ligne (départ, arrivée)..."
                value={valeur}
                onChange={(e) => onChange(e.target.value)}
            />

            {/* Affiche le bouton "Effacer" uniquement si la valeur de recherche n'est pas vide *\/ */}
            {valeur && (
                <button className="btn-effacer" onClick={handleEffacer}>
                    Effacer
                </button>
            )}

        </div>
    );
}

export default Recherche;