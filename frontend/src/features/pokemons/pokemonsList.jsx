import { useGetPokemonsQuery } from "./pokemonsApiSlice";
import { Link } from "react-router-dom";

const PokemonsList = () => {
  const {
    data: pokemons,
    isLoading,
    isSuccess,
    isError,
    error,
  } = useGetPokemonsQuery();

  let content;
  if (isLoading) {
    content = <p>"Loading..."</p>;
  } else if (isSuccess) {
    content = (
      <section className="pokemons">
        <h1>Pokemons List</h1>
        <ul>
          {pokemons.map((pokemon, i) => {
            return <li key={i}>{pokemon.name}</li>;
          })}
        </ul>
        <Link to="/">Back to Home</Link>
      </section>
    );
  } else if (isError) {
    content = <p>{JSON.stringify(error)}</p>;
  }

  return content;
};
export default PokemonsList;
