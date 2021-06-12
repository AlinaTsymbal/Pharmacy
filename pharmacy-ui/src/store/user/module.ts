import { Api } from '@/utils/api';
import {
  GET_ORDER,
  GET_ORDERS,
  GET_USER,
  LOGIN_USER,
  LOGOUT,
  MAKE_ORDER,
} from '@/store/user/actions';
import {
  SET_ORDER, SET_ORDERS, SET_TOKEN, SET_USER,
} from '@/store/user/mutations';
import { setAuthToken, setUserData } from '@/utils/authorization';
import router from '@/router';
import { notification } from 'ant-design-vue';

interface State {
  user: any;
  token: string | null;
  order: any;
  orders: any[];
}

const store: State = {
  user: null,
  token: null,
  order: null,
  orders: [],
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
  orders(state: State) {
    return state.orders;
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
    const params = order.remedies.map((r: any) => ({
      remedy: r.id,
      pharmacy: r.pharmacy,
      amount: r.amount,
    }));
    Api.post('order', { remedies: params })
      .then((response) => {
        router.push('home');
        notification.success({
          message: 'Замовлення офомленно',
          description: 'Замовлення було офомлено. Очікуйте підтрвердження',
          placement: 'topRight',
          duration: 20,
        });
      });
  },
  [LOGOUT]: (context: any) => {
    localStorage.removeItem('auth-token');
    setAuthToken();
    context.commit(SET_USER, null);
    context.commit(SET_TOKEN, null);
    router.push('/home');
  },
  [GET_ORDERS]: (context: any) => {
    Api.get('orders')
      .then((response) => {
        console.log(response.data);
        context.commit(SET_ORDERS, response.data);
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
  [SET_ORDERS](state: State, orders: any[]) {
    state.orders = orders;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
