import RemedyModel from '@/models/RemedyModel.vue';

export default interface MedKitModel {
  id: number;
  name: string;
  description: string;
  remedies: RemedyModel[];
}
