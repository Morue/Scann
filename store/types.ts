export const TYPES = {
    getters: {
      GET_ACCOUNT: 'GET_ACCOUNT',
      GET_JWT: 'GET_JWT',
      GET_HAS_CONNECTION: 'GET_HAS_CONNECTION',
      GET_IDENTIFIED_CONTAINER: 'GET_IDENTIFIED_CONTAINER',
    },
    mutations: {
      // Generic
      RESET_STATE: 'RESET_STATE',
  
      // Auth
      SET_JWT: 'SET_JWT',
  
      // Core
      SET_ACCOUNT: 'SET_ACCOUNT',
      SET_HAS_CONNECTION: 'SET_HAS_CONNECTION',
      SET_IDENTIFIED_CONTAINER: 'SET_IDENTIFIED_CONTAINER',
    },
    actions: {
      // Generic
      RESET_STATE: 'RESET_STATE',
  
      // Auth
      UPDATE_JWT: 'SET_JWT',
      LOGOUT: 'LOGOUT',
  
      // Core
      UPDATE_ACCOUNT: 'UPDATE_ACCOUNT',
      UPDATE_HAS_CONNECTION: 'UPDATE_HAS_CONNECTION',
      UPDATE_IDENTIFIED_CONTAINER: 'UPDATE_IDENTIFIED_CONTAINER',
    },
    modules: {
      AUTH: 'AUTH',
      CORE: 'CORE',
    },
  };
  