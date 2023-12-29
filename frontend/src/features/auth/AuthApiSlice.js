import { apiSlice } from "../../app/api/ApiSlice";

export const authApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        login: builder.mutation({
            query: credentials => ({
                url: '/token/',
                method: 'POST',
                body: { ...credentials }
            })
        }),
        refresh: builder.mutation({
            query: refresh => ({
                url: 'token/refresh/',
                method: 'POST',
                body: { refresh }
            })
        }),
    })
})


export const {
    useLoginMutation,
    useRefreshMutation,
} = authApiSlice