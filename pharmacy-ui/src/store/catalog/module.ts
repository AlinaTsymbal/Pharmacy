import CategoryModel from "@/models/CategoryModel";
import {
  ADD_TO_BASKET,
  GET_CATEGORIES,
  GET_REMEDIES,
  GET_REMEDY_DETAILS
} from "@/store/catalog/actions";
import {Api} from "@/utils/api";
import {
  ADD_BASKET_ITEM,
  SET_CATEGORIES,
  SET_REMEDIES,
  SET_REMEDY_DETAILS
} from "@/store/catalog/mutations";
import RemedyModel from "@/models/RemedyModel";
import {notification} from "ant-design-vue";

interface State {
  categories: CategoryModel[];
  remedies: RemedyModel[];
  basket: RemedyModel[];
  details: RemedyModel[];
}

const store: State = {
  categories: [],
  remedies: [],
  basket: [],
  details: [],
};

const getters = {
  categories(state: State) {
    return state.categories;
  },
  remedies(state: State) {
    return state.remedies;
  },
  basket(state: State) {
    return state.basket;
  },
  details(state: State) {
    return state.details;
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
        queryParams += `category=${id}&`;
      });
      if (params.categories.length > 1) {
        queryParams = queryParams.slice(0, -1);
      }
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
  [ADD_TO_BASKET]: (context: any, remedy: RemedyModel) => {
    if (!context.getters.basket.find(r => r.id === remedy.id)) {
      context.commit(ADD_BASKET_ITEM, remedy);
      notification.success({
        message: 'Товар додано в корзину',
        description: '',
        placement: 'topRight',
        duration: 4.5,
      });
    } else {
      notification.info({
        message: 'Товар вже знаходиться в корзині',
        description: '',
        placement: 'topRight',
        duration: 4.5,
      });
    }
  },
  [GET_REMEDY_DETAILS]: (context: any, id: number) => {
    Api.get(`remedy/${id}`)
      .then((response) => {
        context.commit(SET_REMEDY_DETAILS, response.data);
      });
  }
};

const mutations = {
  [SET_CATEGORIES]: (state: State, categories: CategoryModel[]) => {
    state.categories = categories;
  },
  [SET_REMEDIES]: (state: State, remedies: RemedyModel[]) => {
    state.remedies = remedies;
  },
  [ADD_BASKET_ITEM]: (state: State, remedy: RemedyModel) => {
    state.basket.push(remedy);
  },
  [SET_REMEDY_DETAILS]: (state: State, details: RemedyModel[]) => {
    state.details = details;
  },
};

export default {
  state: store,
  getters,
  actions,
  mutations,
};
