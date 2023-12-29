import React from "react";
import { getPokemons, getPokemonTypes } from "../services/api";

const PokemonCard = ({ pokemonItem, pokemonTypes }) => {
  return (
    <div className="bg-white p-4 rounded-md shadow-md w-full ">
      <img
        src={`img/pokemons/${String(pokemonItem.pokedex_id).padStart(
          3,
          "0"
        )}.png`}
        className="w-full h-auto object-cover mb-4 flex-1"
      />
      <h1 className="text-lg font-semibold mb-2">
        <strong>{pokemonItem.pokedexId}</strong> {pokemonItem.name}
      </h1>
      <p className="text-gray-600">
        {pokemonItem.types.map((pokemonType, index) => (
          <img
            key={pokemonType.id}
            src={`img/types/${pokemonType.name}.png`}
            className="w-auto h-auto object-cover mb-4 flex-1"
          />
        ))}
      </p>
    </div>
  );
};

export default PokemonCard;
