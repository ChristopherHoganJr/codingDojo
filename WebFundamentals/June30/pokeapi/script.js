// Notes
// Promise - 3 states
//    State 1: Pending - Still working
//    State 2: Resolved - Successful
//    State 3: Reject - Failed

// Version 1 to contact APIs
// async function fetchPokemon() {
//   try {
//     var response = await fetch("https://pokeapi.co/api/v2/pokemon/charizard");
//     var data = await response.json();
//     console.log(data);
//   } catch {
//     console.log("it didnt work");
//   }
// }

let pokemonContainer = document.getElementById("pokemonContainer");
let pokeImage = document.getElementById("pokeImg");

// Version 2 to contact APIs
function fetchPokemon(element, event) {
  event.preventDefault();

  var pokemonInput = document.querySelector("#pokemonInput");
  fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonInput.value}`)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      pokemonContainer.innerHTML = makePokemonCard(data);
    })
    .catch((err) => {
      alert("it didnt work");
      console.log(err);
    });
}

//fetchPokemon();

function makePokemonCard(data) {
  let pokeName = data.name.charAt(0).toUpperCase() + data.name.slice(1);
  let statAtributes = "";

  data.stats.forEach((item, idx) => {
    statAtributes += `<li>
                            ${item.stat.name} - ${item.base_stat}
                        </li>`;
  });
  let pokemonTypes = "";
  data.types.forEach((pokeType, idx) => {
    pokemonTypes += `
                        <li>
                            ${pokeType.type.name}
                        </li>
      `;
  });
  let card = `<div class="pokemonCard">
                    <h2 class="pokemonName">${pokeName}</h2>
                    <h2>Pokemon Number: ${data.id}</h2>
                    <img id="pokeImg" src="${data.sprites.front_default}" alt="${data.name} sprite" >
                    <h3>Types</h3>
                    <ul class="types">
                    ${pokemonTypes}
                    </ul>
                    <h3>Stats</h3>
                    <ul>
                    ${statAtributes}
                    </ul>
                </div>`;
  return card;
}
