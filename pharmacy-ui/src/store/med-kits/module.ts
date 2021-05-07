import MedKitModel from '@/models/MedKitModel';
import {GET_MED_KITS} from '@/store/med-kits/actions';
import {SET_MED_KITS} from '@/store/med-kits/mutations';
import RemedyModel from "@/models/RemedyModel";

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
    const remedies: RemedyModel[] = [
      {
        id: 1,
        name: 'Remedy 1',
      },
      {
        id: 2,
        name: 'Remedy 2',
      },
      {
        id: 3,
        name: 'Remedy 3',
      },
      {
        id: 4,
        name: 'Remedy 4',
      },
      {
        id: 5,
        name: 'Remedy 5',
      },
      {
        id: 6,
        name: 'Remedy 6',
      },
    ];
    const kits: MedKitModel[] = [
      {
        id: 1,
        name: 'Med kit 1',
        description: 'Description of med kit 1',
        remedies,
      },
      {
        id: 2,
        name: 'Med kit 2',
        description: 'Description of med kit 2',
        remedies,
      },
      {
        id: 3,
        name: 'Med kit 3',
        description: 'Description of med kit 3',
        remedies,
      },
    ];
    context.commit(SET_MED_KITS, kits);
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
