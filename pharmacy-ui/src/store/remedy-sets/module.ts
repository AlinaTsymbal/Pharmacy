import { Api } from '@/utils/api';
import { ADD_SET_TO_BASKET, GET_REMEDY_SETS } from '@/store/remedy-sets/actions';
import { SET_REMEDY_SETS } from '@/store/remedy-sets/mutations';
import RemedySetModel from '@/models/RemedySetModel';
import { SET_BASKET } from '@/store/catalog/mutations';
import { notification } from 'ant-design-vue';
import router from '@/router';

interface State {
  remedySets: RemedySetModel[];
}

const store: State = {
  remedySets: [],
};

const getters = {
  remedySets(state: State) {
    return state.remedySets;
  },
};

const actions = {
  [GET_REMEDY_SETS]: (context: any) => {
    Api.get('remedy-sets')
      .then((response) => {
        context.commit(SET_REMEDY_SETS, response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  [ADD_SET_TO_BASKET]: (context: any, set: RemedySetModel) => {
    Api.post('basket', { remedies: set.remedies.map((r) => r.id) })
      .then((response) => {
        context.commit(SET_BASKET, response.data);
        notification.success({
          message: 'Набір додано в корзину',
          description: '',
          placement: 'topRight',
          duration: 4.5,
        });
      })
      .catch(() => {
        router.push('authorization');
      });
  },
};

const mutations = {
  [SET_REMEDY_SETS](state: State, kits: RemedySetModel[]) {
    state.remedySets = kits;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
