import RemedyModel from "@/models/RemedyModel";

export default interface RemedySetModel {
  id: number;
  name: string;
  description: string;
  remedies: RemedyModel[];
}
