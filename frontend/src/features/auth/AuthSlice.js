import { createSlice } from "@reduxjs/toolkit"

const authSlice = createSlice({
    name: 'auth',
    initialState: { 
        user: localStorage.getItem('user') || null,
        token: localStorage.getItem('token') || null, 
        refresh: localStorage.getItem('refresh') || null, },
    reducers: {
        setCredentials: (state, action) => {
            const { refresh, access, username } = action.payload
            state.user = username
            state.token = access
            state.refresh = refresh
        },
        logOut: (state, action) => {
            state.user = null
            state.token = null
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            localStorage.removeItem('refresh');
        },
        setTokenCredentials: (state, action) => {
            const { access, username } = action.payload
            state.token = access
            localStorage.setItem('token', access)
        }
    },
})

export const { setCredentials, logOut, setTokenCredentials } = authSlice.actions

export default authSlice.reducer

export const selectCurrentUser = (state) => state.auth.user
export const selectCurrentToken = (state) => state.auth.token
export const selectCurrentRefresh = (state) => state.auth.refresh