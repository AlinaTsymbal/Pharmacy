import MedKitModel from '@/models/MedKitModel';
import { ADD_MED_KIT_TO_BASKET, GET_MED_KITS } from '@/store/med-kits/actions';
import { SET_MED_KITS } from '@/store/med-kits/mutations';
import { Api } from '@/utils/api';
import { SET_BASKET } from '@/store/catalog/mutations';
import { notification } from 'ant-design-vue';
import router from '@/router';

interface State {
  medKits: MedKitModel[];
}

const store: State = {
  medKits: [],
};

const getters = {
  medKits(state: State) {
    return state.medKits;
  },
};

const actions = {
  [GET_MED_KITS]: (context: any) => {
    Api.get('med-kits')
      .then((response) => {
        context.commit(SET_MED_KITS, response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  [ADD_MED_KIT_TO_BASKET]: (context: any, kit: MedKitModel) => {
    Api.post('basket', { remedies: kit.remedies.map((r) => r.id) })
      .then((response) => {
        context.commit(SET_BASKET, response.data);
        notification.success({
          message: 'Аптечку додано в корзину',
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
  [SET_MED_KITS](state: State, kits: MedKitModel[]) {
    state.medKits = kits;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
