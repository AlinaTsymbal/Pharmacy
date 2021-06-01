import {Api} from "@/utils/api";
import {GET_ORDER, GET_USER, LOGIN_USER, MAKE_ORDER} from "@/store/user/actions";
import {SET_ORDER, SET_TOKEN, SET_USER} from "@/store/user/mutations";
import {setUserData} from "@/utils/authorization";
import router from "@/router";

interface State {
  user: any;
  token: string | null;
  order: any;
}

const store: State = {
  user: null,
  token: null,
  order: null,
};

const getters = {
  user(state: State) {
    return state.user;
  },
  token(state: State) {
    return state.token;
  },
  order(state: State) {
    return state.order;
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
  [GET_ORDER]: (context: any, user: any) => {
    Api.get('order', user)
      .then((response) => {
        context.commit(SET_ORDER, response.data);
      });
  },
  [MAKE_ORDER]: (context: any, order: any) => {
    const params = order.remedies.map(r => {
      return {
        remedy: r.id,
        pharmacy: r.pharmacy,
        amount: r.amount,
      };
    });
    Api.post('order', {remedies: params})
      .then((response) => {
        console.log('here')
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
  [SET_ORDER](state: State, order: any) {
    state.order = order;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
