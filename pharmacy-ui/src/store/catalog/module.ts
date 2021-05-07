 import CategoryModel from "@/models/CategoryModel";
import {GET_CATEGORIES} from "@/store/catalog/actions";
import {Api} from "@/utils/api";
import {SET_CATEGORIES} from "@/store/catalog/mutations";

interface State {
  categories: CategoryModel[];
}

const store: State = {
  categories: [],
};

const getters = {
  categories(state: State) {
    return state.categories;
  },
};

const actions = {
  [GET_CATEGORIES]: (context: any) => {
    Api.get('categories')
      .then((response) => {
        context.commit(SET_CATEGORIES, response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  [SET_CATEGORIES]: (state: State, categories: CategoryModel[]) => {
    state.categories = categories;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
