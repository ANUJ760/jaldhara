export const auth = {
  login: () => { localStorage.setItem('token', 'dev-token'); window.location.href = '/dashboard'; },
  logout: () => { localStorage.removeItem('token'); window.location.href = '/login'; },
  isAuthenticated: () => !!localStorage.getItem('token')
};