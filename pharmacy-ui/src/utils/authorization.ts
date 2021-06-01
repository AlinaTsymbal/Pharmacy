import router from "@/router";
import store from '@/store';
import axios from "axios";
import {SET_TOKEN, SET_USER} from "@/store/user/mutations";
import {GET_USER} from "@/store/user/actions";

export const setAuthInterceptor = () => {
  axios.interceptors.response.use((response) => response, (error) => {
    if (error.response.status === 401) {
      localStorage.removeItem('auth-token');
      delete axios.defaults.headers.common.Authorization;

      store.commit(SET_USER, null);
      store.commit(SET_TOKEN, null);

      router.push('/authorization');
    }

    return Promise.reject(error);
  });
};

export const setAuthToken = (token?: string) => {
  if (token) {
    axios.defaults.headers.common.Authorization = token;
  } else {
    delete axios.defaults.headers.common.Authorization;
  }
};

export const setUserData = (context: any, data: any) => {
  const token = `Bearer ${data.access}`;

  localStorage.setItem('auth-token', token);
  setAuthToken(token);
  context.commit(SET_TOKEN, token);
  store.dispatch(GET_USER, token);
};

export const isAuthenticated = (to: any, from: any, next: any) => {
  const token = localStorage.getItem('auth-token');

  if (store.getters.token === null) {
    if (token !== null) {
      store.dispatch(GET_USER, token);
      next();
      return;
    }
    next();
  } else {
    next();
    return;
  }
};
