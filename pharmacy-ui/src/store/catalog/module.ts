import CategoryModel from "@/models/CategoryModel";
import {GET_CATEGORIES, GET_REMEDIES} from "@/store/catalog/actions";
import {Api} from "@/utils/api";
import {SET_CATEGORIES, SET_REMEDIES} from "@/store/catalog/mutations";
import RemedyModel from "@/models/RemedyModel";

interface State {
  categories: CategoryModel[];
  remedies: RemedyModel[];
}

const store: State = {
  categories: [],
  remedies: [],
};

const getters = {
  categories(state: State) {
    return state.categories;
  },
  remedies(state: State) {
    return state.remedies;
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
  [GET_REMEDIES]: (context: any, params: any) => {
    let queryParams = '';
    if (params.categories) {
      queryParams += '?';
      params.categories.forEach(id => {
        queryParams += `category=${id}`;
      });
      delete params.categories;
    }

    Api.get(`remedies${queryParams}`, {params})
      .then((response) => {
        context.commit(SET_REMEDIES, response.data);
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
  [SET_REMEDIES]: (state: State, remedies: RemedyModel[]) => {
    state.remedies = remedies;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
