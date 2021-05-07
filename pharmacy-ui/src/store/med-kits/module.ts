import MedKitModel from '@/models/MedKitModel';
import {GET_MED_KITS} from '@/store/med-kits/actions';
import {SET_MED_KITS} from '@/store/med-kits/mutations';
import {Api} from "@/utils/api";

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
