import Vue from 'vue';

const API_URL = 'http://localhost:8000/api/';

export const Api = {
  get(resource: string, options?: any) {
    return Vue.axios.get(API_URL + resource, options);
  },
  post(resource: string, value: any) {
    return Vue.axios.post(API_URL + resource, value);
  },
  patch(resource: string, value: any) {
    return Vue.axios.patch(API_URL + resource, value);
  },
  delete(resource: string) {
    return Vue.axios.delete(API_URL + resource);
  },
};
