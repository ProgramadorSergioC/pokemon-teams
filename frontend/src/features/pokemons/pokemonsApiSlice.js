import { apiSlice } from "../../app/api/ApiSlice"

export const pokemonsApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPokemons: builder.query({
            query: () => 'pokemons/',
            // keepUnusedDataFor: 5,
        })
    })
})

export const {
    useGetPokemonsQuery
} = pokemonsApiSlice