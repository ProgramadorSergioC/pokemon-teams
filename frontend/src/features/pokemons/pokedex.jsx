import { useState, useEffect } from "react";
import PokemonCard from "../../components/PokemonCard";
import { useGetPokemonsQuery } from "./pokemonsApiSlice";

import { getPokemons } from "../../services/api";

const Pokedex = () => {
  const {
    data: pokemons,
    isLoading,
    isSuccess,
    isError,
    error,
  } = useGetPokemonsQuery();

  const [filteredPokemons, setFilteredPokemons] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    if (isSuccess) {
      setFilteredPokemons(pokemons);
    }
  }, [isSuccess, pokemons]);

  const handleSearch = (term) => {
    setSearchTerm(term);
    console.log(term);
    const filtered = pokemons.filter(
      (pokemon) =>
        pokemon.name.toLowerCase().includes(term.toLowerCase()) ||
        pokemon.types.some(
          (type) => type.name.toLowerCase() == term.toLowerCase()
        )
    );
    setFilteredPokemons(filtered);
  };

  let content;
  if (isLoading) {
    content = <p>"Loading..."</p>;
  } else if (isSuccess) {
    content = (
      <>
        <h1 className="text-3xl text-center font-bold mb-4">Pokedex</h1>
        <div>
          <input
            type="text"
            placeholder="Search Pokemon"
            value={searchTerm}
            onChange={(e) => handleSearch(e.target.value)}
            className="p-2 mb-4 w-full"
          />
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          {filteredPokemons.map((pokemonItem) => (
            <PokemonCard key={pokemonItem.id} pokemonItem={pokemonItem} />
          ))}
        </div>
      </>
    );
  } else if (isError) {
    content = <p>{JSON.stringify(error)}</p>;
  }
  return content;
};

export default Pokedex;
