
import {Api} from "@/utils/api";
import {GET_REMEDY_SETS} from "@/store/remedy-sets/actions";
import {SET_REMEDY_SETS} from "@/store/remedy-sets/mutations";
import RemedySetModel from "@/models/RemedySetModel";

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
