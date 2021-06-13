<template>
  <div class="about-page-wrapper">
    <div class="about">
      <h1>Про сервіс</h1>
    </div>

    <div>
      <div class="about-section-wrapper">
        <span>{{ firstSection }}</span>
      </div>
      <div class="about-section-wrapper">
        <span>{{ secondSection }}</span>
      </div>
      <div class="about-section-wrapper">
        <span>{{ thirdSection }}</span>
      </div>
      <div class="about-section-wrapper-header">
        <span>Служба підтримки</span>
      </div>
      <div class="about-section-wrapper" v-for="s in support">
        <span>{{ s }}</span>
      </div>
      <div class="about-section-wrapper">
        <a href="mailto: orders_P&PLikiv@gmail.com">orders_P&PLikiv@gmail.com</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About',
  data() {
    return {
      firstSection: 'Сервіс П&П Ліків( Пошук та підбір ліків) - інформаційний портал,'
        + ' який дозволяє отримувати інформацію для особистих некомерційних цілей щодо складу,'
        + ' показань, протипоказань, побічних ефектів та цін на лікарські засоби та препарати'
        + ' в аптеках міста Черкаси.',
      secondSection: 'Унікальність сервісу полягає в тому, що на сайті є сторінки зі сформованими'
        + ' наборами ліків, що можна комплексно застосовувати при лікуванні певних недугів та'
        + ' міні-аптечки на різні випадки життя, що сформовані відповідно до призначення.',
      thirdSection: 'Даний сервіс не являється медичним довідником та не містить протоколів'
        + ' лікування певних захворювань. Перед застосуванням будь-якого лікарського препарату'
        + ' проконсультуйтесь з Вашим сімейним лікарем.',
      support: [
        'Час роботи служби підтримки 8:00 — 21:00',
        'Дзвінки згідно з тарифами оператора.',
        '+38-068-123-45-67 - Київстар',
        '+38-063-123-45-67 - Vodafone',
        '+38-050-123-45-67 - life:)',
        'Пропозиції та зауваження просимо надсилати на наш Email',
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.about-page-wrapper {
  div {
    width: 90%;
    justify-content: center;
    margin: auto;

    .about-section-wrapper {
      margin-top: 1rem;

      span {
        font-size: large;
      }
    }

    .about-section-wrapper-header {
      padding: 2rem 0;

      span {
        font-size: 2rem;
      }
    }
  }
}
</style>
