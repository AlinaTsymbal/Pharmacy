import RemedyModel from '@/models/RemedyModel';

export default interface MedKitModel {
  id: number;
  name: string;
  description: string;
  remedies: RemedyModel[];
}
