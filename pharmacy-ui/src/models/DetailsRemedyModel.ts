import RemedyModel from '@/models/RemedyModel';

export default interface DetailsRemedyModel extends RemedyModel {
  structure: string,
  form: string,
  manufacturer: string,
  group: string,
  indication: string,
  contraindication: string,
  application_method: string,
  side_effecnts: string,
}
