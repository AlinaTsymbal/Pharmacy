import {Api} from "@/utils/api";
import {GET_USER, LOGIN_USER} from "@/store/user/actions";
import {SET_TOKEN, SET_USER} from "@/store/user/mutations";
import {setUserData} from "@/utils/authorization";
import router from "@/router";

interface State {
  user: any;
  token: string | null;
}

const store: State = {
  user: null,
  token: null,
};

const getters = {
  user(state: State) {
    return state.user;
  },
  token(state: State) {
    return state.token;
  },
};

const actions = {
  [GET_USER]: (context: any, token: string) => {
    Api.get('me')
      .then((response) => {
        context.commit(SET_USER, response.data);
        context.commit(SET_TOKEN, token);
      });
  },
  [LOGIN_USER]: (context: any, user: any) => {
    Api.post('login', user)
      .then((response) => {

        setUserData(context, response.data);
        router.push('home');
      });
  },
};

const mutations = {
  [SET_USER](state: State, user: any) {
    state.user = user;
  },
  [SET_TOKEN](state: State, token: string | null) {
    state.token = token;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
