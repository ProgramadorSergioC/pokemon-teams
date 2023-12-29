import { createSlice } from "@reduxjs/toolkit"

const authSlice = createSlice({
    name: 'auth',
    initialState: { 
        user: localStorage.getItem('user') || null,
        token: localStorage.getItem('token') || null, 
        refresh: localStorage.getItem('refresh') || null, 
        isAuthenticated: localStorage.getItem('token') || null, },
    reducers: {
        setCredentials: (state, action) => {
            const { refresh, access, username } = action.payload
            state.user = username
            state.token = access
            state.refresh = refresh
            state.isAuthenticated = true
        },
        logOut: (state, action) => {
            console.log("logout")
            state.user = null
            state.token = null
            state.isAuthenticated = false
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
export const isAuthenticated = (state) => state.auth.isAuthenticated