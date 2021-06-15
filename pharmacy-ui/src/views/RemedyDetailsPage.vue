<template>
  <div class="remedy-details-page-wrapper">
    <h1>{{ details.name }}</h1>
    <div class="image-pharmacies-row">
      <div class="image-wrapper">
        <img alt="Remedy image" :src="`data:image/png;base64,${image}`"/>
      </div>
      <div class="prices-wrapper" v-if="pharmacies.length > 0">
        <h2>Можна придбати в:</h2>
        <p v-for="d in pharmacies">
          {{ `${d.details.name} за адресою ${d.details.address} за ціною ${d.price}` }}
        </p>
        <a-button style="margin-top: 14rem" @click="handleClick">Додати в кошик</a-button>
      </div>
    </div>
    <div class="property">
      <h2>Склад:</h2>
      <span v-for="t in structure">{{ t }}</span>
    </div>
    <div class="property">
      <h2>Лікарська форма:</h2>
      <span v-for="t in form">{{ t }}</span>
    </div>
    <div class="property">
      <h2>Виробник:</h2>
      <span v-for="t in manufacturer">{{ t }}</span>
    </div>
    <div class="property">
      <h2>Фармакотерапефтична форма:</h2>
      <span v-for="t in group">{{ t }}</span>
    </div>
    <div class="property">
      <h2>Показання:</h2>
      <span v-for="t in indication">{{ t }}</span>
    </div>
    <div class="property">
      <h2>Протипоказання:</h2>
      <span v-for="t in contraindication">{{ t }}</span>
    </div>
    <div class="property">
      <h2>Спосіб застосування:</h2>
      <span v-for="t in application_method">{{ t }}</span>
    </div>
    <div class="property">
      <h2>Побічні реакції:</h2>
      <span v-for="t in side_effects">{{ t }}</span>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { ADD_TO_BASKET, GET_REMEDY_DETAILS } from '@/store/catalog/actions';

export default {
  name: 'RemedyDetailsPage',
  computed: {
    ...mapGetters([
      'details',
    ]),
    image() {
      return this.details?.image;
    },
    pharmacies() {
      return this.details?.pharmacies;
    },
    application_method() {
      return this.details?.application_method.split('\\n');
    },
    contraindication() {
      return this.details?.contraindication.split('\\n');
    },
    structure() {
      return this.details?.structure.split('\\n');
    },
    form() {
      return this.details?.form.split('\\n');
    },
    manufacturer() {
      return this.details?.manufacturer.split('\\n');
    },
    group() {
      return this.details?.group.split('\\n');
    },
    indication() {
      return this.details?.indication.split('\\n');
    },
    side_effects() {
      return this.details?.side_effects.split('\\n');
    },
  },
  methods: {
    handleClick() {
      this.$store.dispatch(ADD_TO_BASKET, { id: this.$route.params.id });
    },
  },
  mounted() {
    this.$store.dispatch(GET_REMEDY_DETAILS, this.$route.params.id);
  },
};
</script>

<style scoped lang="scss">
.remedy-details-page-wrapper {
  display: flex;
  flex-direction: column;
  width: 80%;
  margin: auto;

  .image-pharmacies-row {
    width: 100%;
    display: flex;
    flex-direction: row;
  }

  .image-wrapper {
    height: 25rem;
    width: 40%;
    margin-right: 10%;
    border: 1px solid lightgray;
    border-radius: 10px;

    img {
      max-width: 100%;
      max-height: 100%;
    }
  }

  .prices-wrapper {
    height: 25rem;
    width: 40%;
    display: flex;
    flex-direction: column;

    h2 {
      text-align: left;
    }

    p {
      text-align: left;
    }
  }

  .property {
    display: flex;
    flex-direction: column;

    span {
      text-align: left;
    }

    h2 {
      text-align: left;
    }
  }

  h1 {
    text-align: left;
  }
}
</style>
